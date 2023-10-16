  from flask import Flask, request, Response
  import time

  app = Flask(__name__)

  def generate_log_updates(log_file):
      # Function to generate log updates
      with open(log_file, 'r') as f:
          while True:
              line = f.readline()
              if not line:
                  time.sleep(1)  # Wait for new content
                  continue
              yield line

  @app.route('/log')
  def stream_log():
      log_file = '/path/to/your/log/file.log'
      return Response(generate_log_updates(log_file), content_type='text/plain')

  if __name__ == '__main__':
      app.run(debug=True)


