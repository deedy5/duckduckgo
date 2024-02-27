import time
import pytest

from duckduckgo_search import DDGS


@pytest.fixture(autouse=True)
def pause_between_tests():
    time.sleep(1)


def test_text():
    with DDGS() as ddgs:
        results = ddgs.text("cat", max_results=30)
        assert len(results) == 30


def test_text_params():
    with DDGS() as ddgs:
        results = ddgs.text("cat", safesearch="off", timelimit="m", max_results=30)
        assert len(results) == 30


def test_text_html():
    with DDGS() as ddgs:
        results = ddgs.text("eagle", backend="html", max_results=30)
        assert len(results) == 30


def test_text_lite():
    with DDGS() as ddgs:
        results = ddgs.text("dog", backend="lite", max_results=30)
        assert len(results) == 30


def test_images():
    with DDGS() as ddgs:
        results = ddgs.images("airplane", max_results=140)
        assert len(results) == 140


def test_videos():
    with DDGS() as ddgs:
        results = ddgs.videos("sea", max_results=40)
        assert len(results) == 40


def test_news():
    with DDGS() as ddgs:
        results = ddgs.news("tesla", max_results=30)
        assert len(results) == 30


def test_maps():
    with DDGS() as ddgs:
        results = ddgs.maps("school", place="London", max_results=30)
        assert len(results) == 30


def test_answers():
    with DDGS() as ddgs:
        results = ddgs.answers("sun")
        assert len(results) >= 1


def test_suggestions():
    with DDGS() as ddgs:
        results = ddgs.suggestions("moon")
        assert len(results) >= 1


def test_translate():
    with DDGS() as ddgs:
        results = ddgs.translate(["school", "tomatoes"], to="de")
        expected_results = [
            {
                "detected_language": "en",
                "translated": "Schule",
                "original": "school",
            },
            {
                "detected_language": "en",
                "translated": "Tomaten",
                "original": "tomatoes",
            }
        ]
        assert all(er in results for er in expected_results)
