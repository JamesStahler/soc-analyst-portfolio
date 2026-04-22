from app.services.title_intelligence import expand_job_titles


def test_soc_expansion_contains_expected_variants():
    titles = expand_job_titles(["SOC Analyst"])
    assert "Security Operations Analyst" in titles
    assert "Cybersecurity Analyst" in titles
