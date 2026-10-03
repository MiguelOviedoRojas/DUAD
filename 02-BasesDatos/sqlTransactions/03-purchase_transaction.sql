
SET search_path TO shop;

DO $$

DECLARE
	v_dni VARCHAR(20);
	v_id_user INTEGER;
	v_products INTEGER[];
	v_quantities INTEGER[];
	v_stock INTEGER;
	v_price NUMERIC(10,2);
	v_id_bill INTEGER;
	i INTEGER;
	v_id_product INTEGER;
	v_quantity INTEGER;
BEGIN

	v_dni := '1111111';
	v_products := ARRAY[1,2];
	v_quantities := ARRAY[1,2];

	SELECT id INTO v_id_user
	FROM users
	WHERE dni = v_dni;

	IF v_id_user IS NULL THEN
		RAISE EXCEPTION 'Usuario no existe';
	END IF;
	
	IF ARRAY_LENGTH(v_products,1) <>
		ARRAY_LENGTH(v_quantities,1) THEN
		
		RAISE EXCEPTION 'Product and quantity counts do not match';
	END IF;
	
	FOR i IN 1 .. ARRAY_LENGTH(v_products,1)
	LOOP
		v_id_product := v_products[i];
		v_quantity := v_quantities[i];
		
		SELECT stock
		INTO v_stock
		FROM products
		WHERE id = v_id_product;
		
		IF NOT FOUND THEN
			RAISE EXCEPTION 'Product % does not exist', v_id_product;
		END IF;
	
		IF v_stock < v_quantity THEN
			RAISE EXCEPTION 'Insufficient stock for product %', v_id_product;
		END IF;
		
	END LOOP;
	
	INSERT INTO BILLS (ID_USER)
	VALUES (v_id_user)
	RETURNING id INTO v_id_bill;
	
	
	FOR i IN 1 .. ARRAY_LENGTH(v_products,1)
	LOOP
		v_id_product := v_products[i];
		v_quantity := v_quantities[i];
		
		SELECT price
		INTO v_price
		FROM products
		WHERE id = v_id_product;
	
		INSERT INTO BILLS_DETAILS (ID_BILL, ID_PRODUCT, QUANTITY, UNIT_PRICE)
		VALUES (v_id_bill, v_id_product, v_quantity, v_price);
	
		UPDATE PRODUCTS
		SET STOCK = STOCK - v_quantity
		WHERE ID = v_id_product;

	END LOOP;
	
END $$;