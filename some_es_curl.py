# 删除index为twitter_xnr_relations doc_type为user id为834571011949469699_923752533268553728 的一条记录
curl -XDELETE 'localhost:9206/twitter_xnr_relations/user/834571011949469699_923752533268553728'

# 查看集群健康状态
curl -XGET localhost:9205/_cluster/health?pretty=true

# 返回信息的关键指标说明
	# status：集群状态，分为green、yellow和red。 
	# number_of_nodes/number_of_data_nodes:集群的节点数和数据节点数。 
	# active_primary_shards：集群中所有活跃的主分片数。 
	# active_shards：集群中所有活跃的分片数。 
	# relocating_shards：当前节点迁往其他节点的分片数量，通常为0，当有节点加入或者退出时该值会增加。 
	# initializing_shards：正在初始化的分片。 
	# unassigned_shards：未分配的分片数，通常为0，当有某个节点的副本分片丢失该值就会增加。 
	# number_of_pending_tasks：是指主节点创建索引并分配shards等任务，如果该指标数值一直未减小代表集群存在不稳定因素 
	# active_shards_percent_as_number：集群分片健康度，活跃分片数占总分片数比例。 
	# number_of_pending_tasks：pending task只能由主节点来进行处理，这些任务包括创建索引并将shards分配给节点。


# 查看集群状态信息，主要包含整个集群的一些统计信息，例如文档数、分片数、资源使用情况等。
curl -XGET localhost:9205/_cluster/stats?pretty

# 返回信息的关键指标说明
	# indices.count：索引总数。 
	# indices.shards.total：分片总数。 
	# indices.shards.primaries：主分片数量。 
	# docs.count：文档总数。 
	# store.size_in_bytes：数据总存储容量。 
	# segments.count：段总数。 
	# nodes.count.total：总节点数。  
	# nodes.count.data：数据节点数。 
	# nodes. process. cpu.percent：节点CPU使用率。 
	# fs.total_in_bytes：文件系统使用总容量。 
	# fs.free_in_bytes：文件系统剩余总容量。

# 节点监控
curl -XGET localhost:9205/_nodes/stats?pretty 
# 返回信息的关键指标说明： 
	# name：节点名。 
	# roles：节点角色。 
	# indices.docs.count：索引文档数。 
	# segments.count：段总数。 
	# jvm.heap_used_percent：内存使用百分比。 
	# thread_pool.{bulk, index, get, search}.{active, queue, rejected}：线程池的一些信息，包括bulk、index、get和search线程池，主要指标有active（激活）线程数，线程queue（队列）数和rejected（拒绝）线程数量。

# 索引监控
curl -XGET localhost:9205/_stats?pretty
# 返回信息的关键指标说明： 

	# indexname.primaries.docs.count：索引文档数量。





curl -XGET localhost:9205/_cluster/health?pretty=true # 查看集群健康状态

curl -XGET "localhost:9205/_cat/indices?v=" | grep red # 查出红的索引

curl -XDELETE 'http://192.168.169.47:9206/group_message_2019-07-02' #根据索引名删除索引

curl -XGET localhost:9205/_cat/shards | grep UNASSIGNED # 查看有问题的分片 没有被分配的分片

curl 'localhost:9205/_nodes/process?pretty'           # 查看结点的信息 包括id等信息

# index有问题分片的索引名 shard 编号 通过查找有问题的分片的命令会给出  node 主节点的唯一标识
curl -XPOST 'localhost:9205/_cluster/reroute' -d '{"commands" : [ {"allocate" : {"index" : "weibo_xnr","shard" : 2,"node" : "ixrP7jYYROaGTdbtGkmlgg","allow_primary" : true}}] }' # 重新分配索引分片








  