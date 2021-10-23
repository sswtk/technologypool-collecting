/**
 * @Author: roninsswang
 * @Date: 2021/10/23 11:13 下午
 * @File: server_proxy
 */

package server_proxy

import (
	"net/rpc"
	"rpc_go_implement/new_helloworld/handler"
)

type HelloServicer interface{
	Hello(request string, reply *string) error
}

func RegisterHelloService(srv HelloServicer) error {
	return rpc.RegisterName(handler.HelloServiceName, srv)
}