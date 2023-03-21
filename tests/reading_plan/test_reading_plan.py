from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
from tests.assets.news import NEWS
import pytest
from unittest.mock import patch

answer_mock = {
    "readable": [
        {"unfilled_time": 1, "chosen_news": [("noticia_0", 2)]},
        {
            "unfilled_time": 1,
            "chosen_news": [("Notícia bacana 2", 1), ("noticia_3", 1)],
        },
        {
            "unfilled_time": 1,
            "chosen_news": [("noticia_4", 1), ("noticia_5", 1)],
        },
        {"unfilled_time": 2, "chosen_news": [("noticia_6", 1)]},
    ],
    "unreadable": [
        ("Notícia bacana", 4),
        ("noticia_7", 7),
        ("noticia_8", 8),
        ("noticia_9", 5),
    ],
}


def test_reading_plan_group_news():
    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(0)

    def news_mock():
        return NEWS

    with patch("tech_news.analyzer.reading_plan.find_news", news_mock):
        reading_plan_service = ReadingPlanService()
        response = reading_plan_service.group_news_for_available_time(3)
        assert response == answer_mock
