require 'digest/sha1'
require 'google/cloud/language'
require 'hashie'
require 'logging'
require 'mongoid'
require 'news-api'
require 'nokogiri'
require 'parallel'
require 'rest-client'

# Setup ENV vars
require 'dotenv/load'

# Setup Mongoid
Mongoid.load!('./mongoid.yml', :development)
# Mongo::Logger.logger = Logger.new($stdout, :debug)
# Mongo::Logger.logger.level = Logger::DEBUG

# This class is from the news-api library. #name refers the #site the article is from..
class Everything
  alias site name
end

# require models
Dir['./models/*'].each { |path| require_relative path }
Dir['./models/news_parser/*'].each { |path| require_relative path }
