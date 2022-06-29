export const networkScanConfigurationSchema  = {
  'type': 'object',
  'additionalProperties': false,
  'properties': {
    'fingerprinters': {
      'title': 'Fingerprinters',
      'type': 'array',
      'items': {
      '$ref': '#/definitions/plugins'
      },
      'default': [
        {'name': 'SMBFinger', 'safe': true, 'options': {}},
        {'name': 'SSHFinger', 'safe': true, 'options': {}},
        {'name': 'HTTPFinger', 'safe': true, 'options': {}},
        {'name': 'MSSQLFinger', 'safe': true, 'options': {}},
        {'name': 'ElasticFinger', 'safe': true, 'options': {}}
      ]
    },
    'icmp': {
      '$ref': '#/definitions/icmp_scan',
      'type': 'object'
    },
    'targets': {
      '$ref': '#/definitions/scan_target',
      'type': 'object'
    },
    'tcp': {
      '$ref': '#/definitions/tcp_scan',
      'type': 'object'
    }

  }
}
