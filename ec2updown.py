import sys
import boto.ec2

def show_usage():
  '''
  shows usage for script
  '''
  print 'example ...'
  print '$ python ec2updown.py tag up'
  print '   :tag: - name of tag value for filtering'
  print '   :param: up|down - powers instances up or down'
  print ''
  sys.exit(1)

def getInstances(tag, ec2_conn):
  '''
  gets only instances that include the passed tag

  :param: tag: tag used to filter instances
  '''

  name_filter = '%s*' % tag 
  instances = ec2_conn.get_only_instances(filters={'tag-value': name_filter})

  return instances

def updown(verb, instances, ec2_conn):
  '''
  turns on(up)/off(down) all instnaces returned in filter

  :param: updown: up|down specified to bring instances up or down
  '''
  for i in instances:
    print str(i.tags)

def main():
  if len(sys.argv) < 3:
    show_usage()
  
  tag = sys.argv[1]
  verb = sys.argv[2]
  ec2_conn = boto.ec2.connection.EC2Connection()
  instances = getInstances(tag, ec2_conn)
  updown(verb, instances, ec2_conn)

if __name__ == "__main__":
  main()
