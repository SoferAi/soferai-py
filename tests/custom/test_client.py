import os
import time
import uuid
from datetime import datetime

import pytest

from soferai import SoferAI, SoferAIEnvironment
from soferai.health.types.health_response import HealthResponse
from soferai.link.types.link_response import LinkResponse
from soferai.transcribe.types.transcription import Transcription
from soferai.transcribe.types.transcription_id import TranscriptionId
from soferai.transcribe.types.transcription_info import TranscriptionInfo
from soferai.transcribe.types.transcription_request_info import (
    TranscriptionRequestInfo,
)


@pytest.mark.incremental
@pytest.mark.skipif(
    condition=os.getenv("SOFERAI_API_KEY") is None,
    reason="This is a test for the production environment, and requires a valid API key",
)
@pytest.mark.skipif(
    condition=os.getenv("SKIP_CLIENT_TESTS") == "true",
    reason="Skipping client tests in CI",
)
class TestSoferAIProd:
    TEST_UUID: uuid.UUID = uuid.uuid4()  # this is overwritten in a test

    # Make sure your API key is set in the environment variable SOFERAI_API_KEY
    client: SoferAI = SoferAI(environment=SoferAIEnvironment.PRODUCTION)

    def test_health(self) -> None:
        # this just tests that the api is up and taking requests
        response: HealthResponse = self.client.health.get_health()
        assert response.status == "ok"

    def test_link_extract(self) -> None:
        # this is the API frontend for `torah-dl`
        response: LinkResponse = self.client.link.extract(
            url="https://www.yutorah.org/lectures/1116616/Praying-for-Rain-and-the-International-Traveler"
        )
        assert (
            response.download_url
            == "https://download.yutorah.org/2024/986/1116616/praying-for-rain-and-the-international-traveler.mp3"
        )
        assert response.file_format == "audio/mp3"
        assert response.file_name == "praying-for-rain-and-the-international-traveler.mp3"
        assert response.title == "Praying for Rain and the International Traveler"

    def test_transcription_simple(self) -> None:
        # this is a simple runthrough of the transcription API, with no fancy features
        transcription_id: TranscriptionId = self.client.transcribe.create_transcription(
            audio_url="https://drive.google.com/uc?export=download&id=1_hSFDw_8Ps8uSMfmR9wgo8Xx92gJj_RA",
            info=TranscriptionRequestInfo(),
        )
        assert transcription_id is not None

        # wait for the transcription to complete
        for _ in range(60):
            status_response: TranscriptionInfo = self.client.transcribe.get_transcription_status(
                transcription_id=transcription_id
            )

            assert status_response.status in [
                "RECEIVED",
                "PENDING",
                "PROCESSING",
                "COMPLETED",
            ]
            if status_response.status == "COMPLETED":
                break
            time.sleep(2)
        else:
            raise AssertionError("Transcription did not complete within 60 seconds")

        # get the transcription
        response: Transcription = self.client.transcribe.get_transcription(
            transcription_id=transcription_id,
        )
        assert response.info.status == "COMPLETED"
        assert response.text is not None

    def test_create_transcription(self) -> None:
        # this is the same as the simple transcription test, but with a custom info object
        info: TranscriptionRequestInfo = TranscriptionRequestInfo(
            id=self.TEST_UUID,
            title=f"test_prod_{datetime.now().strftime('%Y%m%d%H%M%S')}",
            primary_language="en",
            hebrew_word_format=[
                "en",
                "he",
            ],
            num_speakers=1,
        )
        response: TranscriptionId = self.client.transcribe.create_transcription(
            audio_url="https://drive.google.com/uc?export=download&id=1_hSFDw_8Ps8uSMfmR9wgo8Xx92gJj_RA", info=info
        )

        assert response is not None
        assert response != ""
        assert isinstance(response, uuid.UUID)
        assert response == self.TEST_UUID

    def test_get_transcription_status(self) -> None:
        for _ in range(60):
            response: TranscriptionInfo = self.client.transcribe.get_transcription_status(
                transcription_id=self.TEST_UUID
            )

            assert response.status in [
                "RECEIVED",
                "PENDING",
                "PROCESSING",
                "COMPLETED",
            ]
            if response.status == "COMPLETED":
                return
            time.sleep(1)
        else:
            raise AssertionError("Transcription did not complete within 60 seconds")

    def test_get_transcription_complex(self) -> None:
        response: Transcription = self.client.transcribe.get_transcription(
            transcription_id=self.TEST_UUID,
        )
        assert response.info.status == "COMPLETED"
        assert response.text is not None
