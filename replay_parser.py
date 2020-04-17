# coding=utf-8
import json
import logging
import os
from json import JSONEncoder

from replay_unpack.clients import wot, wows
from replay_unpack.replay_decrypt import WoWSReplayDecrypt, ReplayInfo

logging.basicConfig(
    level=logging.ERROR
)


class DefaultEncoder(JSONEncoder):
    def default(self, o):
        try:
            return o.__dict__
        except AttributeError:
            return str(o)


class ReplayParser(object):
    BASE_PATH = os.path.dirname(__file__)

    def __init__(self, replay_path, strict: bool = False):
        self._replay_path = replay_path
        self._is_strict_mode = strict
        self._decrypter = WoWSReplayDecrypt(replay_path)

    def get_info(self):
        replay = self._decrypter.get_replay_data()

        error = None
        try:
            hidden_data = self._get_hidden_data(replay)
        except Exception as e:
            if isinstance(e, RuntimeError):
                error = str(e)
            logging.exception(e)
            hidden_data = None

            # raise error in strict mode
            if self._is_strict_mode:
                raise

        return dict(
            open=replay.engine_data,
            extra_data=replay.extra_data,
            hidden=hidden_data,
            error=error
        )

    def _get_hidden_data(self, replay: ReplayInfo):
        # more than enough almost always
        client_version = '.'.join(replay.version[:3])
        if replay.game == 'wotreplay':
            player = wot.ReplayPlayer(client_version)
        elif replay.game == 'wowsreplay':
            player = wows.ReplayPlayer(client_version)
        else:
            raise NotImplementedError
        player.play(replay.decrypted_data, self._is_strict_mode)
        return player.get_info()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--replay', type=str, required=True)
    parser.add_argument(
        '--log_level',
        choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'],
        required=False,
        default='ERROR'
    )
    parser.add_argument(
        '--strict_mode',
        action='store_true',
        required=False
    )

    namespace = parser.parse_args()
    logging.basicConfig(
        level=getattr(logging, namespace.log_level))
    replay_info = ReplayParser(
        namespace.replay, strict=namespace.strict_mode).get_info()
    print(json.dumps(replay_info, indent=1, cls=DefaultEncoder))
