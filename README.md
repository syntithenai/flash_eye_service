A simple web service to flash the red LED on a Sony Playstation Eye webcam.
I am using it to flash the light when a spoken hotword is detected.
Implemented using the command ```timeout 1 cat /dev/video0```

## SOS Endpoint

### /sos

- Flashes the red LED in the Morse code pattern for SOS (three short, three long, three short).
- Usage: `GET /sos`
- Response: `Flashed SOS pattern.` (HTTP 200)

Example:
```
curl http://localhost:5021/sos
```
