
Byte = {
    'LF': '\x0A',
    'NULL': '\x00'
}


class WsFrame:

    def __init__(self, command, headers, body):
        self.command = command
        self.headers = headers
        self.body = body

    def __str__(self):
        if self.command == Byte['LF']:
            return self.command

        lines = [self.command]
        skipContentLength = 'content-length' in self.headers
        if skipContentLength:
            del self.headers['content-length']

        for name in self.headers:
            value = self.headers[name]
            lines.append("" + name + ":" + value)

        if self.body is not None and not skipContentLength:
            lines.append("content-length:" + str(len(self.body)))

        if self.body is not None:
            lines.append(Byte['LF'] + self.body)
        else:
            lines.append(Byte['LF'])

        return Byte['LF'].join(lines)

    @staticmethod
    def unmarshall_single(data):
        lines = data.split(Byte['LF'])
        command = lines[0].strip()
        if command == '':
            command = "PONG"
            return WsFrame(command, {}, None)
        headers = {}

        # get all headers
        i = 1
        while lines[i] != '':
            # get key, value from raw header
            (key, value) = lines[i].split(':')
            headers[key] = value
            i += 1

        # set body to None if there is no body
        body = None if lines[i + 1] == Byte['NULL'] else lines[i + 1][:-1]

        return WsFrame(command, headers, body)

    @staticmethod
    def marshall(command, headers, body):
        return str(WsFrame(command, headers, body)) + Byte['NULL']
