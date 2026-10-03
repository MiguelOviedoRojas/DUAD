SET search_path TO shop;

DO $$

DECLARE

	v_id_bill INTEGER;
	v_state VARCHAR(15);
	
	i RECORD;

BEGIN
	v_id_bill := 1;
	
	SELECT state INTO v_state
	FROM BILLS
	WHERE id = v_id_bill;
	
	IF NOT FOUND THEN
		RAISE EXCEPTION 'Invoice does not exist';
	END IF;
	
	IF v_state = 'RETURNED' THEN
		RAISE EXCEPTION 'Invoice has already been returned';
	END IF;
	
	FOR i IN
	(
		SELECT id_product,
				quantity
		FROM BILLS_DETAILS
		WHERE id_bill = v_id_bill
	)
	LOOP
		
		UPDATE products
		SET stock = stock + i.quantity
		WHERE id = i.id_product;
	
	END LOOP;
	
		UPDATE bills
		SET state = 'RETURNED'
		WHERE id = v_id_bill;
	
END $$