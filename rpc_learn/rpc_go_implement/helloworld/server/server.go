/**
 * @Author: roninsswang
 * @Date: 2021/10/17 10:44 上午
 * @File: server
 */

package main

import (
	"net"
	"net/rpc"
)

type HelloService struct {}

func (s *HelloService) Hello(request string, reply *string) error{
	// 返回值是通过修改reply的值
	*reply = "hello " + request
	return nil
}

func main() {
	//实例化server
	listener, _ := net.Listen("tcp", ":1234")
	//注册处理逻辑
	_ = rpc.RegisterName("HelloService", &HelloService{})
	//启动服务
	conn, _ := listener.Accept()
	rpc.ServeConn(conn)
}