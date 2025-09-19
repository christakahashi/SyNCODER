import json

s1fp = "ACAACGCTCAAATCAGGG"
s1rp = "GTGACGGTAGGTGAAATC"
s1rp_rc = "GATTTCACCTACCGTCAC"
JSON_template_mandatory = \
"""
{
  "id": null,
  "seq": {
    "osizemin": null,
    "osizemedian": null,
    "osizemax": null,
    "orepmin": null,
    "orepmax": null,
    "ocount": null,
    "adapter": false,
    "natural": true,
    "coverageinfo": "30x"
  },
  "codec": {
    "id": null,
    "vendor": "UW MISL",
    "name": "SyNCODER",
    "ver": null,
    "uri": "http://misl.bio",
    "params": {}
  },
  "vendorid": null
}
"""

JSON_template_optional = \
"""
{
  "desc": null,
  "hash": {
    "alg": "SHA256",
    "val": null,
    "addl": {}
  },
  "ts": null,
  "vendor": {
    "name": "UW MISL",
    "uri": "http://misl.bio",
    "contact": null
  },
  "opt": {}
}
"""

def get_sector_1_obj():
  return json.loads(JSON_template_mandatory)

