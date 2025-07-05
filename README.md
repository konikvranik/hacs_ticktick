# TickTick TODO Integration for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

This custom component integrates [TickTick](https://ticktick.com/) todo lists with Home Assistant's [Todo integration](https://www.home-assistant.io/integrations/todo/), allowing you to view and manage your TickTick tasks directly from Home Assistant.

## Features

- View and manage TickTick tasks from Home Assistant
- Create new tasks
- Update existing tasks
- Delete tasks
- Set task descriptions
- Set due dates for tasks
- Each TickTick project appears as a separate todo list entity in Home Assistant

## Requirements

- Home Assistant 2023.8.0 or newer (with Todo integration support)
- A TickTick account
- TickTick API credentials (Client ID and Client Secret)

## Installation

### HACS Installation (Recommended)

1. Make sure you have [HACS](https://hacs.xyz/) installed in your Home Assistant instance.
2. Add this repository as a custom repository in HACS:
   - Go to HACS in your Home Assistant instance
   - Click on "Integrations"
   - Click the three dots in the top right corner
   - Select "Custom repositories"
   - Add the URL `https://github.com/konikvranik/hacs_ticktick`
   - Select "Integration" as the category
   - Click "Add"
3. Search for "TickTick TODO" in HACS and install it
4. Restart Home Assistant

### Manual Installation

1. Download the latest release from the [GitHub repository](https://github.com/konikvranik/hacs_ticktick)
2. Create a `custom_components` directory in your Home Assistant configuration directory if it doesn't already exist
3. Extract the `ticktick_todo` directory from the release into the `custom_components` directory
4. Restart Home Assistant

## Configuration

### Step 1: Obtain TickTick API Credentials

1. Go to the [TickTick Developer Portal](https://developer.ticktick.com/)
2. Create a new application
3. Set the redirect URI to `https://my.home-assistant.io/redirect/oauth` if you're using My Home Assistant, or to your Home Assistant URL followed by `/auth/external/callback` (e.g., `https://your-home-assistant:8123/auth/external/callback`)
4. Note down the Client ID and Client Secret

### Step 2: Add the Integration to Home Assistant

1. Go to Home Assistant Settings > Devices & Services
2. Click "Add Integration" and search for "TickTick TODO"
3. Click on the integration and follow the configuration flow
4. Enter your Client ID and Client Secret when prompted
5. Authorize the application with your TickTick account

## Usage

After setting up the integration, each of your TickTick projects will appear as a separate todo list entity in Home Assistant. You can:

- View your tasks in the Home Assistant UI
- Create new tasks
- Mark tasks as completed
- Update task details
- Delete tasks

### Example Automations

#### Create a new task when something happens

```yaml
automation:
  - alias: "Create TickTick task when motion detected"
    trigger:
      - platform: state
        entity_id: binary_sensor.motion_sensor
        to: "on"
    action:
      - service: todo.add_item
        target:
          entity_id: todo.ticktick_your_project_id
        data:
          item: "Check why there was motion"
          due_date: "{{ now().strftime('%Y-%m-%d') }}"
```

#### Mark a task as completed based on a condition

```yaml
automation:
  - alias: "Mark watering plants task as done when moisture is detected"
    trigger:
      - platform: numeric_state
        entity_id: sensor.plant_moisture
        above: 60
    action:
      - service: todo.update_item
        target:
          entity_id: todo.ticktick_your_project_id
        data:
          item: "Water the plants"
          status: "completed"
```

## Troubleshooting

### Authentication Issues

If you encounter authentication issues:

1. Go to Home Assistant Settings > Devices & Services
2. Find the TickTick TODO integration and click "Configure"
3. Follow the steps to reauthorize the application

### Missing Projects or Tasks

- Make sure your TickTick account has the correct permissions
- Try restarting Home Assistant
- Check the Home Assistant logs for any error messages

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms of the license specified in the repository.

## Links

- [Home Assistant Community Discussion](https://community.home-assistant.io/)
- [GitHub Repository](https://github.com/konikvranik/hacs_ticktick)
- [Issue Tracker](https://github.com/konikvranik/hacs_ticktick/issues)