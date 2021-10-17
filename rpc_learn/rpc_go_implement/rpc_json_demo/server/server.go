/**
 * @Author: roninsswang
 * @Date: 2021/10/17 4:32 下午
 * @File: server
 */

package main

import (
	"net"
	"net/rpc"
	"net/rpc/jsonrpc"
)

type HelloService struct {}

func (s *HelloService) Hello(request string, reply *string) error{
	// 返回值是通过修改reply的值
	*reply = "hello " + request
	return nil
}

func main() {
	listener, _ := net.Listen("tcp", ":1234")
	_ = rpc.RegisterName("HelloService", &HelloService{})
	for {
		conn, _ := listener.Accept()
		go rpc.ServeCodec(jsonrpc.NewServerCodec(conn))
	}
}