from COMMON_DATA import API_FILENAME
import os, time, datetime, logger

def check_api_commands():
  time_modified = time.ctime(os.path.getmtime(API_FILENAME))
  # print("last modified: %s" % time_modified)

  time_array = time_modified.split(" ")
  # print(time_array[1] + " " + time_array[2] + " " + time_array[4])
  file_time_stamp = time_array[1] + " " + time_array[2] + " " + time_array[4]

  current_time_stamp = datetime.datetime.now().strftime("%b %d %Y")
  #print(current_time_stamp)

  if (current_time_stamp != file_time_stamp):
    open(API_FILENAME, "w").close()
    logger.log("ERASED", "c")

  else:
    logger.log("NOT ERASED", "c")
