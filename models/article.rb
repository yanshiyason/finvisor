class Article
  include Mongoid::Document
  field :uuid, type: String
  field :data, type: Hash
  field :meta, type: Hash

  validates_uniqueness_of :uuid

  index({ uuid: 1 }, unique: true)
end

# make sure indexes are create when file is required
Article.create_indexes
