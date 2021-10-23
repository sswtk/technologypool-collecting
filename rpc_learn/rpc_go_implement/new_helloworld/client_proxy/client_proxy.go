/**
 * @Author: roninsswang
 * @Date: 2021/10/23 10:41 下午
 * @File: client_proxy
 */

package client_proxy

import (
	"net/rpc"
	"rpc_go_implement/new_helloworld/handler"
)

type HelloServiceStub struct{
	*rpc.Client
}

func NewHelloServiceClient (protcol, address string) HelloServiceStub{
	conn, err := rpc.Dial(protcol, address)
	if err != nil{
		panic("Connect Error……")
	}
	return HelloServiceStub{conn}
}

func (c *HelloServiceStub) Hello(request string, reply *string) error {
	err := c.Call(handler.HelloServiceName+".Hello", request, reply)
	if err != nil {
		return err
	}
	return nil
}


