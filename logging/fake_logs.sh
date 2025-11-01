import sys

print("Oops something went wrong", file=sys.stderr)


while true; do
  echo "INFO: User login successful at $(date)" > log_pipe
  sleep 1
  echo "ERROR: Disk usage high! at $(date)" > log_pipe
  sleep 2
done


while true; do
  echo "INFO: User login successful at $(date)"
  sleep 1
  echo "ERROR: Disk usage high! at $(date)"
  sleep 2
done
