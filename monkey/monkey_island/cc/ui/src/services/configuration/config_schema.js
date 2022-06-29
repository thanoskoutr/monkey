import {customPBAConfigurationSchema} from './definitions/custom_pbas.js';
import {pluginConfigurationSchema} from './definitions/plugins.js';
import {exploitationConfigurationSchema} from './definitions/exploitation.js';
import {exploitationOptionsConfigurationSchema} from './definitions/exploitation_options.js';
import {icmpScanConfigurationSchema} from './definitions/icmp_scan.js';
import {tcpScanConfigurationSchema} from './definitions/tcp_scan.js';
import {scanTargetConfigurationSchema} from './definitions/scan_target.js';
import {propagationConfigurationSchema} from './definitions/propagation.js';
import {networkScanConfigurationSchema} from './definitions/network_scan.js';

export const SCHEMA = {
  'title': 'Monkey',
  'type': 'object',
  'definitions': {
    'custom_pbas': customPBAConfigurationSchema,
    'plugins': pluginConfigurationSchema,
    'exploitation': exploitationConfigurationSchema,
    'exploitation_options': exploitationOptionsConfigurationSchema,
    'icmp_scan': icmpScanConfigurationSchema,
    'tcp_scan': tcpScanConfigurationSchema,
    'scan_target': scanTargetConfigurationSchema,
    'propagation': propagationConfigurationSchema,
    'network_scan': networkScanConfigurationSchema
  },
  'properties': {
    'general': {
      'title': 'General',
      'type': 'object',
      'properties':{
        'keep_tunnel_open_time': {
          'title': 'Keep tunnel open time',
          'format': 'float',
          'type': 'number',
          'default': 30,
          'description': 'Time to keep tunnel open before going down after last exploit (in seconds)'
        }
      }
    },
    'propagation': {
      'title': 'Propagation',
      '$ref': '#/definitions/propagation',
      'type': 'object'
    },
    'post_breach_actions': {
      'title': 'Post-breach actions',
      'type': 'object',
      'properties': {
        'pba_list': {
          'title': 'PBAs',
          'type': 'array',
          'items': {
            '$ref': '#/definitions/plugins'
          },
          'default': [
            {'name': 'CommunicateAsBackdoorUser','safe': true, 'options': {}},
            {'name': 'ModifyShellStartupFiles', 'safe': true, 'options': {}}
          ]
        },
        'custom_pbas': {
          'title': 'Custom post-breach action',
          '$ref': '#/definitions/custom_pbas',
          'type': 'object'
        }
      }
    },
    'payloads': {
      'title': 'Payloads',
      'type': 'array',
      'items': {
        '$ref': '#/definitions/plugins'
      },
      'default': [
        {'name': 'ransomware', 'safe': true, 'options': {}}
      ]
    },
    'credential_collectors': {
      'title': 'Credential collectors',
      'type': 'array',
      'items': {
        '$ref': '#/definitions/plugins'
      },
      'default': [
        {'name': 'MimikatzCollector', 'safe': true, 'options':{}},
        {'name': 'SSHCollector', 'safe': true, 'options':{}}
      ]
    }
  },
  'options': {'collapsed': true}
}
