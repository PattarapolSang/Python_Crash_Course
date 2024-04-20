import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions"""
    question    = "What is your first language you learn"
    language_survey = AnonymousSurvey(question)

    return language_survey


def test_survey_report(language_survey):

    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_survey_list(language_survey):

    language_list   = ["English", "Spanish", "Thai"]
    for language in language_list:
        language_survey.store_response(language)

    for item in language_list:
        assert item in language_survey.responses