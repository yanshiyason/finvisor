require 'forwardable'

class MainLogger
  @logger = Logging.logger[self]
  @logger.level = :debug

  @logger.add_appenders \
    Logging.appenders.stdout,
    Logging.appenders.file('logs/development.log')

  class << self
     extend Forwardable
     def_delegators :@logger, :fatal, :warn, :debug, :info, :error
  end
end
