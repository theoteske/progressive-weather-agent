import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error message.
    """
    if city.lower() == "los angeles":
        return {
            "status": "success",
            "report": (
                "The weather in Los Angeles is cloudy with a temperature of 15 degrees"
                " Celsius (59 degrees Fahrenheit)."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for {city} is not available.",
        }
    
def get_current_time(city: str) -> dict:
    """Retrieves the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error message.
    """
    if city.lower() == "los angeles":
        tz_identifier = "America/Los_Angeles"
    else:
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }
    
    timezone = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(timezone)
    report = (
        f"The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}."
    )
    return {
            "status": "success",
            "report": report,
        }

root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the weather and time in a city."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the weather"
        " and time in a city."
    ),
    tools=[get_weather, get_current_time],
)