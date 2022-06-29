export const propagationConfigurationSchema = {
  'additionalProperties': false,
  'type': 'object',
  'properties': {
    'exploitation': {
      '$ref': '#/definitions/exploitation',
      'type': 'object'
    },
    'maximum_depth': {
      'title': 'Maximum scan depth',
      'type': 'integer',
      'minimum': 1,
      'default': 2,
      'description': 'Amount of hops alloed for the monkey to spread from the ' +
      'Island server. \n' +
      ' \u26A0' +
      ' Note that setting this value too high may result in the ' +
      'Monkey propagating too far, '+
      'if the "Local network scan" is enabled'
    },
    'network_scan': {
      '$ref': '#/definitions/network_scan',
      'type': 'object'
    }
  }
}
