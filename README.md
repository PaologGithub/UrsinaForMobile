# Ursina For Mobile  
### The New Era of Ursina Gaming on Android

[![GitHub issues](https://img.shields.io/github/issues/PaologGithub/UrsinaForMobile)](https://github.com/PaologGithub/UrsinaForMobile/issues)
[![GitHub forks](https://img.shields.io/github/forks/PaologGithub/UrsinaForMobile)](https://github.com/PaologGithub/UrsinaForMobile/network)
[![GitHub stars](https://img.shields.io/github/stars/PaologGithub/UrsinaForMobile)](https://github.com/PaologGithub/UrsinaForMobile/stargazers)
[![License](https://img.shields.io/github/license/PaologGithub/UrsinaForMobile)](LICENSE)

## Overview

Ever wanted to export your Ursina game for Android? Now you can!  
**Ursina For Mobile** brings the power of the Ursina engine to Android devices.  
> **Note:**  
> Currently, only Android is supported. iOS is not supported due to Panda3D limitations and testing constraints (i.e., lack of macOS/iOS hardware).

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running Your Game](#running-your-game)
- [Documentation](#documentation)
- [Community and Support](#community-and-support)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)
- [License](#license)

---

## Features

- **Android Support:** Export and run your Ursina games on Android devices.
- **Seamless Integration:** Follow detailed instructions and scripts for porting.
- **Community Driven:** Join discussions and issues to help evolve the project.

---

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- [Python 3.7+](https://www.python.org/downloads/)
- [Ursina Engine](https://github.com/pokepetter/ursina)
- Android SDK & Build Tools (for packaging)

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/PaologGithub/UrsinaForMobile.git
   cd UrsinaForMobile
   ```
2. **Set Up Your Environment:**
   - Create a virtual environment (optional but recommended):
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

### Running Your Game

Follow the detailed steps in our [documentation](/docs/docs.md) to:
- Configure your Android project.
- Package your Ursina game for Android.
- Troubleshoot common issues.

---

## Documentation

For full details on how to port your game for Android, visit our [comprehensive documentation](/docs/docs.md). It covers:
- Step-by-step setup instructions.
- Environment configuration.
- Build and deployment procedures.

---

## Community and Support

If you encounter any issues or need help:
- **Issues:** Report bugs or feature requests by opening an [issue](https://github.com/PaologGithub/UrsinaForMobile/issues).
- **Discussions:** Join our [discussions](https://github.com/PaologGithub/UrsinaForMobile/discussions) for community support.
- **Discord:** For real-time help, join the [Ursina Engine Discord](https://discord.com/invite/ydXfhyb).

---

## Contributing

Contributions are welcome! Here’s how you can get involved:
1. **Fork the repository.**
2. **Create a new branch:**  
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit your changes** with clear and concise messages.
4. **Push your branch** and create a pull request.

You can also contribute by reporting issues and suggesting improvements.

---

## Acknowledgments

Special thanks to:
- **pokepetter** – for creating the Ursina Engine.
- **Panda3D Developers** – for their continuous support and development of Panda3D.
- **rdb (RenderBear)** – for assistance with Panda3D integration.
- **The Community** – for testing and contributing to the project.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
