

bind = "0.0.0.0:8000"
workers = 2
threads = 2
timeout = 120
loglevel = "info"

# Logging config
accesslog = None     # "-" nghĩa là log ra stdout
errorlog = "-"      # log lỗi ra stderr
capture_output = True  # ghi stdout/stderr từ app