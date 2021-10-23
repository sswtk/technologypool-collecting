/**
 * @Author: roninsswang
 * @Date: 2021/10/23 10:03 下午
 * @File: handler
 */

package handler


const HelloServiceName = "handler/HelloService"

type NewHelloService struct {}

func (s *NewHelloService) Hello(request string, reply *string) error{
	*reply = "hello, " + request
	return nil
}