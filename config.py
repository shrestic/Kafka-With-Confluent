config = {
    "google_api_key": "<your key>",
    "youtube_playlist_id": "PLr3-bEi1N4khKZm2u6Q8pOLO-WNZrKDHn",
    "kafka": {
        "bootstrap.servers": "<your serve>",
        "security.protocol": "sasl_ssl",
        "sasl.mechanism": "PLAIN",
        "sasl.username": "<your key>",
        "sasl.password": "<your secret>",
    },
    "schema_registry": {
        "url": "<your SR server>",
        "basic.auth.user.info": "<your SR key>:<your SR secret>",
    }
}