from brainzutils import cache
from brainzutils.musicbrainz_db.recording import fetch_multiple_recordings
from critiquebrainz.frontend.external.musicbrainz_db import DEFAULT_CACHE_EXPIRATION


def get_recording_by_id(mbid):
    """Get recording with MusicBrainz ID.

    Args:
        mbid (uuid): MBID(gid) of the recording.
    Returns:
        Dictionary containing the recording information
    """
    key = cache.gen_key(mbid)
    recording = cache.get(key)
    if not recording:
        recording = fetch_multiple_recordings(
            [mbid],
            includes=['artists', 'work-rels', 'url-rels'],
        ).get(mbid)
        cache.set(key=key, val=recording, time=DEFAULT_CACHE_EXPIRATION)
    return recording