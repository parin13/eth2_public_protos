python3.6 -m grpc_tools.protoc -I../../protos --python_out=. --grpc_python_out=. ../../protos/beacon_chain.proto


compile all in one  >> 

python3.6 -m grpc_tools.protoc -I../../protos --python_out=. --grpc_python_out=. ../../protos/*.proto
