import serial
import time

def send_raw_characters(port, baudrate, number_list, delay=1):
    """
    Opens the specified serial port and sends raw characters based on ASCII values.

    Args:
        port (str): Serial port (e.g., '/dev/ttyACM0').
        baudrate (int): Baud rate for the serial communication.
        number_list (list): List of integers (0-255) representing ASCII values to send.
        delay (float): Delay (in seconds) between sending each character.
    """
    try:
        # Open the serial port
        with serial.Serial(port, baudrate, timeout=1) as ser:
            print(f"Connected to {port} at {baudrate} baud.")
            
            for num in number_list:
                if 0 <= num <= 255:
                    # Convert number to raw character and send it
                    raw_char = bytes([num])
                    ser.write(raw_char)
                    print(f"Sent ASCII {num} as {repr(raw_char)}")

                    # Wait before sending the next character
                    time.sleep(delay)
                else:
                    print(f"Invalid number: {num}. Must be between 0 and 255.")

    except KeyboardInterrupt:
        print("Stopped by user.")

if __name__ == "__main__":
    # Configuration
    serial_port = "/dev/ttyACM0"
    baud_rate = 115200
    ascii_values_to_send = [35, 80, 67, 79, 83, 84, 77, 48, 48, 48, 82, 84, 77, 73,49, 49, 55, 57, 55, 59 ]  # Example: 'A', 'B', 'C', rare characters
    send_delay = 0  # Half a second delay

    # Run the function
    send_raw_characters(serial_port, baud_rate, ascii_values_to_send, send_delay)