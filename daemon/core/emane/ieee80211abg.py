"""
ieee80211abg.py: EMANE IEEE 802.11abg model for CORE
"""

from core.emane import emanemanifest
from core.emane import emanemodel


class EmaneIeee80211abgModel(emanemodel.EmaneModel):
    # model name
    name = "emane_ieee80211abg"

    # mac configuration
    mac_library = "ieee80211abgmaclayer"
    mac_xml = "/usr/share/emane/manifest/ieee80211abgmaclayer.xml"
    mac_defaults = {
        "pcrcurveuri": "/usr/share/emane/xml/models/mac/ieee80211abg/ieee80211pcr.xml",
    }
    mac_config = emanemanifest.parse(mac_xml, mac_defaults)
