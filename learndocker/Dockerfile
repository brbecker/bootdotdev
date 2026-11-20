# This is a comment

# Use a lightweight debian os
# as the base image
FROM debian:stable-slim

# Set the port
ENV PORT=8991

# COPY source destination
COPY goserver /bin/goserver

# execute the 'goserver' binary when the container runs
CMD ["/bin/goserver"]
