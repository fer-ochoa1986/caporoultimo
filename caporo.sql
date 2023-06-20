-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-05-2023 a las 01:43:43
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `caporo`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `depilación`
--

CREATE TABLE `depilación` (
  `Tecnica` varchar(20) NOT NULL,
  `Precio` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `depilación`
--

INSERT INTO `depilación` (`Tecnica`, `Precio`) VALUES
('Descartable', 4000),
('Española', 4500),
('Perfilado', 3500),
('Primix', 5000),
('Roll On', 3300);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `manicura_uñas`
--

CREATE TABLE `manicura_uñas` (
  `Diseño` varchar(40) NOT NULL,
  `Precio` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `manicura_uñas`
--

INSERT INTO `manicura_uñas` (`Diseño`, `Precio`) VALUES
('Acrilica', 2200),
('Francesa', 1500),
('Rusa', 2500),
('Semipermanente', 2800),
('Soft Gel', 3000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `venta`
--

CREATE TABLE `venta` (
  `Producto` varchar(20) NOT NULL,
  `Cantidad` int(100) NOT NULL,
  `Precio` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `venta`
--

INSERT INTO `venta` (`Producto`, `Cantidad`, `Precio`) VALUES
('Crema depiladora hom', 30, 800),
('DEPIKIT', 38, 4500),
('Esmalte', 100, 2100),
('Esmaltes Gel', 75, 2000),
('Gel NAVI (uñas)', 60, 3000),
('KIT 1 DEPIMIEL', 25, 17000),
('Kit 2 DEPIMIEL', 10, 20000),
('Kit cera depilatoria', 20, 12000),
('Lampara UV uñas gel', 2, 20800),
('Oleos DEPIMIEL', 35, 4000),
('Piedra Depiladora', 6, 4000),
('Torno para uñas', 10, 6000),
('Torno pulidora de uñ', 4, 12000),
('Uñas Postizas', 100, 3000);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `depilación`
--
ALTER TABLE `depilación`
  ADD PRIMARY KEY (`Tecnica`);

--
-- Indices de la tabla `manicura_uñas`
--
ALTER TABLE `manicura_uñas`
  ADD PRIMARY KEY (`Diseño`);

--
-- Indices de la tabla `venta`
--
ALTER TABLE `venta`
  ADD PRIMARY KEY (`Producto`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
