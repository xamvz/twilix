from twilix.stanzas import Message

class Delay(Message):
    """
    Message-inheritor class for chat history messages in multi-user chat.
    """
    # XXX: WTF?
    elementName = 'delay'
    elementUri = 'urn:xmpp:delay'