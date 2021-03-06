#! /usr/bin/env python

LOGIN_REQUEST_MESSAGE = "login_req"
LOGIN_ACCEPTED_MESSAGE = "login_ack"
LOGIN_REJECTED_MESSAGE = "login_rej"
LOGOUT_REQUEST_MESSAGE = "logout_req"
LOGGED_OUT_MESSAGE = "logged_out"

NEW_ORDER_MESSAGE = "new"
MODIFY_ORDER_MESSAGE = "mod"
CANCEL_ORDER_MESSAGE = "cxl"
ORDER_ACCEPTED_MESSAGE = "ack"
ORDER_REJECTED_MESSAGE = "rej"
MODIFY_ACCEPTED_MESSAGE = "mod_ack"
MODIFY_REJECTED_MESSAGE = "mod_rej"
CANCEL_ACCEPTED_MESSAGE = "cxl_ack"
CANCEL_REJECTED_MESSAGE = "cxl_rej"
CANCEL_ALL_MESSAGE = "cxl_all"
EXECUTION_MESSAGE = "exec"

SYMBOL_STATUS_MESSAGE = "symbol"
MARKET_STATUS_MESSAGE = "market"

ORDER_ADDED_MESSAGE = "added"
ORDER_MODIFIED_MESSAGE = "modified"
ORDER_CANCELED_MESSAGE = "canceled"
ORDER_EXECUTED_MESSAGE = "executed"
TRADE_EXECUTED_MESSAGE = "traded"

CREATE_ENGINE_MESSAGE = "create_engine"
DELETE_ENGINE_MESSAGE = "delete_engine"
SET_ENGINE_PROPERTY_MESSAGE = "set_engine_property"
START_ENGINE_MESSAGE = "start_engine"
STOP_ENGINE_MESSAGE = "stop_engine"

CREATE_ENDPOINT_MESSAGE = "create_endpoint"
DELETE_ENDPOINT_MESSAGE = "delete_endpoint"
SET_ENDPOINT_PROPERTY_MESSAGE = "set_endpoint_property"


class Message(object):
    def __init__(self):
        self.type = None
        return


class LoginRequestMessage(Message):
    def __init__(self):
        self.type = LOGIN_REQUEST_MESSAGE
        self.username = ''
        self.password = ''
        return

class LoginAcceptedMessage(Message):
    def __init__(self):
        self.type = LOGIN_ACCEPTED_MESSAGE
        return

class NewOrderMessage(Message):
    def __init__(self):
        self.type = NEW_ORDER_MESSAGE
        self.symbol = ''
        self.order_type = ''
        self.quantity = 0
        self.price = 0
        return




class CreateEngineMessage(Message):
    def __init__(self):
        self.type = CREATE_ENGINE_MESSAGE
        self.name = ''
        return

class DeleteEngineMessage(Message):
    def __init__(self):
        self.type = DELETE_ENGINE_MESSAGE
        self.name = ''
        return

class SetEnginePropertyMessage(Message):
    def __init__(self):
        self.type = SET_ENGINE_PROPERTY_MESSAGE
        self.engine = ''
        self.name = ''
        self.value = None
        return

class StartEngineMessage(Message):
    def __init__(self):
        self.type = START_ENGINE_MESSAGE
        self.engine = ''
        return

class StopEngineMessage(Message):
    def __init__(self):
        self.type = STOP_ENGINE_MESSAGE
        self.engine = ''
        return

