/**
 * @Author: roninsswang
 * @Date: 2021/10/23 10:02 下午
 * @File: server
 */

package main

import (
	"net"
	"net/rpc"

	"rpc_go_implement/new_helloworld/handler"
	"rpc_go_implement/new_helloworld/server_proxy"
)


func main() {
	//实例化server
	listener, _ := net.Listen("tcp", ":1234")
	//注册处理逻辑
	_ = server_proxy.RegisterHelloService(&handler.NewHelloService{})
	//启动服务
	for {
		conn, _ := listener.Accept()
		go rpc.ServeConn(conn)
	}
}