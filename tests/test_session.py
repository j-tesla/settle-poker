from settle_poker import Session, Transaction


def test_empty_session():
    session = Session()
    result = session.settle()
    assert len(list(result)) == 0


def test_flat_session():
    session = Session()
    session.add_user('a')
    session.add_user('b')
    session.add_buy_in('a', 50)
    session.add_buy_in('b', 50)
    session.cash_out('a', 50)
    session.cash_out('b', 50)
    result = session.settle()
    assert len(list(result)) == 0


def test_single_transaction():
    session = Session()
    session.add_user('a')
    session.add_user('b')
    session.add_buy_in('a', 50)
    session.add_buy_in('b', 50)
    session.cash_out('a', 100)
    session.cash_out('b', 0)
    result = list(session.settle())
    assert len(result) == 1
    assert result[0] == Transaction('b', 'a', 50)

