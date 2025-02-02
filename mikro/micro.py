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
    ascii_values_to_send = [0x23,0x50, 0x43, 0x30, 0x53, 0x54, 0x4D, 0x30, 0x30,   0x32, 0x57, 0x54, 0x4D, 0x49,0xFF,0x26,0x00,0x34,0x39,0x38,0x34,0x33, 0x3B]  # Example: 'A', 'B', 'C', rare characters
    send_delay = 0  # Half a second delay

    # Run the function
    send_raw_characters(serial_port, baud_rate, ascii_values_to_send, send_delay)

    """ getting MI [0x23, 0x50, 0x43, 0x30, 0x53, 0x54, 0x4D, 0x30,   0x30, 0x30, 0x52, 0x54, 0x4D, 0x49, 0x32, 0x30,
0x33, 0x38, 0x36, 0x3B] 
setting 0x23,0x50, 0x43, 0x30, 0x53, 0x54, 0x4D, 0x30, 0x30,   0x32, 0x57, 0x54, 0x4D, 0x49,0xFF,0x26,0x34,0x34,0x39,0x38,0x34,0x33, 0x3B
"""