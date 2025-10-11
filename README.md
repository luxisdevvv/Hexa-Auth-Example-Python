# LUXISDEV License System

A professional license validation system with HexaAuth integration and beautiful terminal interface.

## Features

- **Secure License Validation** - HexaAuth API integration
- **Beautiful Terminal UI** - RGB colors and centered text
- **HWID Protection** - Hardware-based device locking
- **Time Tracking** - Real-time license expiration display
- **Cross Platform** - Windows, Linux, macOS support

## Quick Start

### Installation

```bash
git clone https://github.com/luxisdevvv/Hexa-Auth-Example-Python.git
cd hexa-auth-example-python
pip install -r requirements.txt
```

### Usage

```bash
python main.py
```

## Requirements

- Python 3.7+
- requests
- colorama

## Configuration

Replace `secret_key_goes_here` in `main.py` with your actual HexaAuth secret key:

```python
client = HexaAuthClient("https://hexaauth.alwaysdata.net/api.php", "your_secret_key_here")
```

## Features Overview

### License Validation
- Real-time license checking
- HWID-based device locking
- Automatic time calculation
- Status monitoring

### Terminal Interface
- Centered text alignment
- RGB color support
- Loading animations
- Professional design

## API Response

The system displays:
- **HWID**: Hardware identification
- **Time Left**: Remaining license time
- **Status**: License state (Active/Expired)

## Development

### Project Structure
```
luxisdev-license-system/
├── main.py              # Main application
├── requirements.txt     # Dependencies
└── README.md          # Documentation
```

### Dependencies
- `requests` - HTTP API calls
- `colorama` - Terminal colors
- `os` - System operations
- `time` - Loading animations

## Security

- Secret keys are not exposed in client code
- HWID-based device locking
- Secure API communication
- Input validation

## License Information

This system integrates with HexaAuth for:
- License key validation
- Device count management
- Expiration tracking
- Usage monitoring

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=luxisdevvv/Hexa-Auth-Example-Python&type=Date)](https://star-history.com/#luxisdevvv/Hexa-Auth-Example-Python&Date)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [HexaAuth](https://hexaauth.alwaysdata.net/) for license management
- [Colorama](https://github.com/tartley/colorama) for terminal colors
- [Requests](https://github.com/psf/requests) for HTTP operations

---

<div align="center">

**Star this repository if you found it helpful!**

Made with love by [LUXISDEV](https://github.com/luxisdevvv)

</div>




