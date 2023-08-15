# AutoGPT Flutter Client

## Description

This repository contains the Flutter client for the AutoGPT project. The application allows users to have multiple conversations with agents to resolve various issues. The app is built to be cross-platform and runs on Web, Android, iOS, Windows, and Mac.

## Features

- List and manage multiple agents
- Engage in chat conversations with selected agents
- Configure user settings through a dedicated settings view

## Requirements

- Flutter 3.x
- Dart 3.x

## Installation

1. **Clone the repo:**
```
git clone https://github.com/yourusername/auto_gpt_flutter_client.git
```

2. **Navigate to the project directory:**
```
cd auto_gpt_flutter_client
```

3. **Get Flutter packages:**
```
flutter pub get
```

4. **Run the app:**
```
flutter run
```

## Project Structure

- `lib/`: Contains the main source code for the application.
- `models/`: Data models that define the structure of the objects used in the app.
- `views/`: The UI components of the application.
- `viewmodels/`: The business logic and data handling for the views.
- `services/`: Contains the service classes that handle communication with backend APIs and other external data sources. These services are used to fetch and update data that the app uses, and they are consumed by the ViewModels.
- `test/`: Contains the test files for unit and widget tests.

## Responsive Design

The app features a responsive design that adapts to different screen sizes and orientations. On larger screens (Web, Windows, Mac), views are displayed side by side horizontally. On smaller screens (Android, iOS), views are displayed in a tab bar controller layout.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

