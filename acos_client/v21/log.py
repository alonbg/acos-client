

import base

class Log(base.BaseV21):

        def set(self, sys_log, **kwargs):
            params = { "sys_log": sys_log }
            return self._post("system.log.set", params, **kwargs)

        def get(self, **kwargs):
            return self._get("system.log.get", **kwargs)

        def clear(self, sys_log, **kwargs):
            return self._post("system.log.clear", **kwargs)

        def download(self, **kwargs):
            return self._get('system.log.download', **kwargs)

        def backup(self, **kwargs):
            return self._post('system.log.backup', **kwargs)

        @property
        def level(self):
            return self.Level(self.client)

        class Level(base.BaseV21):
            def get(self, **kwargs):
                return self._get('system.log.level.get', **kwargs)

            def set(self, log_level, **kwargs):
                params = { "log_level" : log_level }
                return self._post('system.log.level.set', params, **kwargs)

        class Server(base.BaseV21):
            def get(self, **kwargs):
                return self._get('system.log.server.get', **kwargs)

            def set(self, log_server, **kwargs):
                params = { "log_server" : log_server }
                return self._post('system.log.server.set', params, **kwargs)

        class Buffer(base.BaseV21):
            def get(self, **kwargs):
                return self._get('system.log.buffer.get', **kwargs)

            def set(self, buff_size, **kwargs):
                params = { "buffer_size" : buff_size }
                return self._post('system.log.buffer.set', params, **kwargs)

        class Smtp(base.BaseV21):
            def get(self, **kwargs):
                return self._get('system.log.smtp.get', **kwargs)

            def set(self, smtp, **kwargs):
                params = { "smtp" : smtp }
                return self._post('system.log.smtp.set', params, **kwargs)

        class Audit(base.BaseV21):
            def get(self, **kwargs):
                return self._get('system.log.audit.get', **kwargs)

            def set(self, audit, **kwargs):
                params = { "audit" : audit }
                return self._post('system.log.audit.set', params, **kwargs)