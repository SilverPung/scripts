import serial

def read_serial_data(port='/dev/ttyACM0', baudrate=115200):
    try:
        # Open the serial port
        ser = serial.Serial(port, baudrate, timeout=1)
        print(f"Listening on {port} at {baudrate} baud...")
        
        while True:
            # Read one byte from the serial port
            data = ser.read()
            
            if data:
                # Convert the byte to its ASCII value
                ascii_value = ord(data)
                print(f"Received: {data.decode('utf-8', errors='ignore')} | ASCII Value: {ascii_value}")
                if ascii_value == 59:
                    print("----"*10)
    
    except serial.SerialException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nExiting program.")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Serial port closed.")

if __name__ == "__main__":
    read_serial_data()