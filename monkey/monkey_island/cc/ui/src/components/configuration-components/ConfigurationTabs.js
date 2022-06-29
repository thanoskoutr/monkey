const CONFIGURATION_TABS = {
  GENERAL: 'general',
  PROPAGATION: 'propagation',
  PAYLOADS: 'payloads',
  PBA: 'post_breach_actions',
  CREDENTIALS_COLLECTORS: 'credential_collectors'
};

const advancedModeConfigTabs = [
  CONFIGURATION_TABS.GENERAL,
  CONFIGURATION_TABS.PROPAGATION,
  CONFIGURATION_TABS.PAYLOADS,
  CONFIGURATION_TABS.PBA,
  CONFIGURATION_TABS.CREDENTIALS_COLLECTORS
];

const ransomwareModeConfigTabs = [
  CONFIGURATION_TABS.GENERAL,
  CONFIGURATION_TABS.PROPAGATION,
  CONFIGURATION_TABS.PAYLOADS
];

const CONFIGURATION_TABS_PER_MODE = {
  'advanced': advancedModeConfigTabs,
  'ransomware': ransomwareModeConfigTabs
};

export default CONFIGURATION_TABS_PER_MODE;
