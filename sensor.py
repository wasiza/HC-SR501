import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

motion_pin = 18
GPIO.setup(motion_pin, GPIO.IN)

def cleanup():
    GPIO.cleanup()

def main():
    threshold = 0.5  # Adjust this threshold based on your needs
    consecutive_detections = 0

    try:
        while True:
            motion_detected = GPIO.input(motion_pin)
            
            if motion_detected:
                consecutive_detections += 1
                print(f"{time.strftime('%d-%m-%Y %H:%M:%S')} - Motion detected!")
            else:
                consecutive_detections = 0
                print(f"{time.strftime('%d-%m-%Y %H:%M:%S')} - No motion detected.")
            
            if consecutive_detections >= threshold * 2:
                print("Motion sustained!")
            
            time.sleep(1)  # Adjust the delay between readings

    except KeyboardInterrupt:
        print("Exiting...")
        cleanup()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("An error occurred:", e)
        cleanup()
