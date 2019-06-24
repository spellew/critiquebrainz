# -*- coding: utf-8 -*-
from unittest import TestCase
from unittest.mock import MagicMock
from critiquebrainz.frontend.external.musicbrainz_db import entities as mb_entities
from critiquebrainz.frontend.external.musicbrainz_db.tests import setup_cache
from brainzutils.musicbrainz_db import release_group as mb_release_group
from brainzutils.musicbrainz_db import recording as mb_recording
from brainzutils.musicbrainz_db import artist as mb_artist
from brainzutils.musicbrainz_db import label as mb_label
from brainzutils.musicbrainz_db import place as mb_place
from brainzutils.musicbrainz_db import event as mb_event
from brainzutils.musicbrainz_db import work as mb_work
from brainzutils.musicbrainz_db.test_data import (
    releasegroup_collision_course,
    releasegroup_numb_encore,
    recording_numb_encore_explicit,
    recording_numb_encore_instrumental,
    artist_linkin_park,
    artist_jay_z,
    label_dreamville,
    label_roc_a_fella,
    place_verkatehdas,
    place_suisto,
    event_ra_hall_uk,
    taubertal_festival_2004,
    work_aquemini,
    work_a_lot,
)


class EntityTestCase(TestCase):

    def setUp(self):
        setup_cache()
        self.setup_queries()
        self.setup_expected()

    def setup_queries(self):
        mb_release_group.mb_session = MagicMock()
        mb_recording.mb_session = MagicMock()
        mb_artist.mb_session = MagicMock()
        mb_label.mb_session = MagicMock()
        mb_place.mb_session = MagicMock()
        mb_event.mb_session = MagicMock()
        mb_work.mb_session = MagicMock()

        self.release_group_query = mb_release_group.mb_session.return_value.\
            __enter__.return_value.query.return_value.options.return_value.\
            options.return_value.options.return_value.options.return_value.\
            options.return_value.filter.return_value.all 
        self.recording_query = mb_recording.mb_session.return_value.\
            __enter__.return_value.query.return_value.options.return_value.\
            filter.return_value.all
        self.artist_query = mb_artist.mb_session.return_value.__enter__.\
            return_value.query.return_value.options.return_value.filter.\
            return_value.all
        self.label_query = mb_label.mb_session.return_value.__enter__.\
            return_value.query.return_value.options.return_value.options.\
            return_value.filter.return_value.all
        self.place_query = mb_place.mb_session.return_value.__enter__.\
            return_value.query.return_value.options.return_value.options.\
            return_value.filter.return_value.all  
        self.event_query = mb_event.mb_session.return_value.__enter__.\
            return_value.query.return_value.filter.return_value.all
        self.work_query = mb_work.mb_session.return_value.__enter__.\
            return_value.query.return_value.options.return_value.filter.\
            return_value.all

    def setup_expected(self):
        self.expected = {
            "8ef859e3-feb2-4dd1-93da-22b91280d768": ("release_group", {
                "id": "8ef859e3-feb2-4dd1-93da-22b91280d768",
                "title": "Collision Course",
                "first-release-year": 2004,
                "type": "EP",
                "artist-credit-phrase": "Jay-Z/Linkin Park",
                "artist-credit": [
                    {
                        "name": "Jay-Z",
                        "artist": {
                            "id": "f82bcf78-5b69-4622-a5ef-73800768d9ac",
                            "name": "JAY Z",
                            "sort_name": "JAY Z"
                        },
                        "join_phrase": "/"
                    },
                    {
                        "name": "Linkin Park",
                        "artist": {
                            "id": "f59c5520-5f46-4d2c-b2c4-822eabf53419",
                            "name": "Linkin Park",
                            "sort_name": "Linkin Park"
                        }
                    }
                ]
            }),
            "7c1014eb-454c-3867-8854-3c95d265f8de": ("release_group", {
                "id": "7c1014eb-454c-3867-8854-3c95d265f8de",
                "title": "Numb/Encore",
                "first-release-year": 2004,
                "type": "Single",
                "artist-credit-phrase": "Jay-Z/Linkin Park",
                "artist-credit": [
                    {
                        "name": "Jay-Z",
                        "artist": {
                            "id": "f82bcf78-5b69-4622-a5ef-73800768d9ac",
                            "name": "JAY Z",
                            "sort_name": "JAY Z"
                        },
                        "join_phrase": "/"
                    },
                    {
                        "name": "Linkin Park",
                        "artist": {
                            "id": "f59c5520-5f46-4d2c-b2c4-822eabf53419",
                            "name": "Linkin Park",
                            "sort_name": "Linkin Park"
                        }
                    }
                ]
            }),
            "daccb724-8023-432a-854c-e0accb6c8678": ("recording", {
                "id": "daccb724-8023-432a-854c-e0accb6c8678",
                "name": "Numb/Encore (explicit)",
                "artist": "Jay-Z/Linkin Park",
                "length": 205.28,
            }),
            "965b75df-397d-4395-aac8-de11854c4630": ("recording", {
                "id": "965b75df-397d-4395-aac8-de11854c4630",
                "name": "Numb/Encore (instrumental)",
                "artist": "Jay-Z/Linkin Park",
                "length": 207.333,
            }),
            "f59c5520-5f46-4d2c-b2c4-822eabf53419": ("artist", {
                "id": "f59c5520-5f46-4d2c-b2c4-822eabf53419",
                "name": "Linkin Park",
                "sort_name": "Linkin Park",
                "type": "Group",
            }),
            "f82bcf78-5b69-4622-a5ef-73800768d9ac": ("artist", {
                "id": "f82bcf78-5b69-4622-a5ef-73800768d9ac",
                "name": "JAY Z",
                "sort_name": "JAY Z",
                "type": "Person",
            }),
            "1aed8c3b-8e1e-46f8-b558-06357ff5f298": ("label", {
                "id": "1aed8c3b-8e1e-46f8-b558-06357ff5f298",
                "name": "Dreamville",
                "type": "Imprint",
                "area": "United States",
            }),
            "4cccc72a-0bd0-433a-905e-dad87871397d": ("label", {
                "id": "4cccc72a-0bd0-433a-905e-dad87871397d",
                "name": "Roc-A-Fella Records",
                "type": "Original Production",
                "area": "United States",
            }),
            "d71ffe38-5eaf-426b-9a2e-e1f21bc84609": ("place", {
                "id": "d71ffe38-5eaf-426b-9a2e-e1f21bc84609",
                "name": "Suisto",
                "type": "Venue",
                "address": "Verkatehtaankuja 7, FI-13200 Hämeenlinna, Finland",
                "coordinates": {
                    "latitude": 60.997758,
                    "longitude": 24.477142
                },
                "area": {
                    "id": "4479c385-74d8-4a2b-bdab-f48d1e6969ba",
                    "name": "Hämeenlinna"
                },
            }),
            "f9587914-8505-4bd1-833b-16a3100a4948": ("place", {
                "id": "f9587914-8505-4bd1-833b-16a3100a4948",
                "name": "Verkatehdas",
                "address": "Paasikiventie 2, FI-13200 Hämeenlinna, Finland",
                "type": "Venue",
                "coordinates": {
                    "latitude": 60.99727,
                    "longitude": 24.47651
                },
                "area": {
                    "id": "4479c385-74d8-4a2b-bdab-f48d1e6969ba",
                    "name": "Hämeenlinna"
                },
            }),
            "40e6153d-a042-4c95-a0a9-b0a47e3825ce": ("event", {
                "id": "40e6153d-a042-4c95-a0a9-b0a47e3825ce",
                "name": "1996-04-17: Royal Albert Hall, London, England, UK",
            }),
            "ebe6ce0f-22c0-4fe7-bfd4-7a0397c9fe94": ("event", {
                "id": "ebe6ce0f-22c0-4fe7-bfd4-7a0397c9fe94",
                "name": "Taubertal-Festival 2004, Day 1",
            }),
            "54ce5e07-2aca-4578-83d8-5a41a7b2f434": ("work", {
                "id": "54ce5e07-2aca-4578-83d8-5a41a7b2f434",
                "name": "a lot",
                "type": "Song",
            }),
            "757504fb-a130-4b84-9eb5-1b37164f12dd": ("work", {
                "id": "757504fb-a130-4b84-9eb5-1b37164f12dd",
                "name": "Aquemini",
                "type": "Song",
            }),
        }

    def update_expected(self, expected, type):
        if (type == "recording"):
            expected.update({ "length": expected["length"] * 1000.0 })
        return expected

    def test_get_entity_by_id(self):
        self.release_group_query.return_value = [releasegroup_numb_encore, releasegroup_collision_course]
        self.recording_query.return_value = [recording_numb_encore_explicit, recording_numb_encore_instrumental]
        self.artist_query.return_value = [artist_linkin_park, artist_jay_z]
        self.label_query.return_value = [label_dreamville, label_roc_a_fella]
        self.place_query.return_value = [place_suisto, place_verkatehdas]
        self.event_query.return_value = [taubertal_festival_2004, event_ra_hall_uk]
        self.work_query.return_value = [work_a_lot, work_aquemini]

        for mbid in self.expected:
            type = self.expected[mbid][0]
            expected = self.update_expected(self.expected[mbid][1], type)
            actual = mb_entities.get_entity_by_id(mbid, type)
            self.assertDictEqual(expected, actual)

    def test_get_multiple_entities(self):
        self.release_group_query.return_value = [releasegroup_numb_encore, releasegroup_collision_course]
        self.recording_query.return_value = [recording_numb_encore_explicit, recording_numb_encore_instrumental]
        self.artist_query.return_value = [artist_linkin_park, artist_jay_z]
        self.label_query.return_value = [label_dreamville, label_roc_a_fella]
        self.place_query.return_value = [place_suisto, place_verkatehdas]
        self.event_query.return_value = [taubertal_festival_2004, event_ra_hall_uk]
        self.work_query.return_value = [work_a_lot, work_aquemini]

        entity_tuples = [(mbid, self.expected[mbid][0]) for mbid in self.expected.keys()]
        multiple_entities = mb_entities.get_multiple_entities(entity_tuples)
        for mbid in self.expected:
            expected = self.expected[mbid][1]
            actual = multiple_entities[mbid]
            self.assertDictEqual(expected, actual)
