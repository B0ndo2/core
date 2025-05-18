"""Test tasks for the LLM Task integration."""

import pytest

from homeassistant.components.llm_task import async_run_task
from homeassistant.core import HomeAssistant


async def test_run_task_unknown_entity(
    hass: HomeAssistant,
    init_components: None,
) -> None:
    """Test running a task with an unknown entity."""

    with pytest.raises(
        ValueError, match="LLM Task entity llm_task.unknown_entity not found"
    ):
        await async_run_task(
            hass, "llm_task.unknown_entity", "summarize", "Test prompt"
        )
