-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-06-2023 a las 03:16:18
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
-- Base de datos: `sistemaclinicafinalparaprogramacion`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `consulta`
--

CREATE TABLE `consulta` (
  `IDConsulta` bigint(20) NOT NULL,
  `IDTurnero` bigint(20) NOT NULL,
  `Diagnostico` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `consultorio`
--

CREATE TABLE `consultorio` (
  `IDConsultorio` bigint(20) NOT NULL,
  `consultorio` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historialclinico`
--

CREATE TABLE `historialclinico` (
  `IDHistorialClinico` bigint(20) NOT NULL,
  `historialPaciente` varchar(50) NOT NULL,
  `ultimaActualizacion` date NOT NULL,
  `IDConsulta` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `horariosmedicos`
--

CREATE TABLE `horariosmedicos` (
  `IDTurnoMedico` bigint(20) NOT NULL,
  `horarioMedico` datetime NOT NULL,
  `IDMedico` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medicos`
--

CREATE TABLE `medicos` (
  `IDMedicos` bigint(20) NOT NULL,
  `nombre` text NOT NULL,
  `apellido` text NOT NULL,
  `fechaNacimiento` date NOT NULL,
  `genero` enum('Femenino','Masculino','Otro') NOT NULL,
  `cuit` bigint(20) NOT NULL,
  `telefonoCelular` int(11) NOT NULL,
  `correoElectronico` varchar(50) NOT NULL,
  `barrio` varchar(50) NOT NULL,
  `calle` text NOT NULL,
  `numero` bigint(20) NOT NULL,
  `pais` varchar(50) NOT NULL,
  `provincia` varchar(50) NOT NULL,
  `especialidad` enum('Cardiólogo','Gastroentrólogo','Neumonólogo','Neurólogo','Pediatra','Trumatólogo','Endocrinólogo','Oncólogo','Radiólogo') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pacientes`
--

CREATE TABLE `pacientes` (
  `IDPacientes` bigint(20) NOT NULL,
  `nombre` text NOT NULL,
  `apellido` text NOT NULL,
  `fechaNacimiento` date NOT NULL,
  `genero` enum('Femenino','Masculino','Otro') NOT NULL,
  `cuit` bigint(20) NOT NULL,
  `telefonoCelular` int(11) NOT NULL,
  `correoElectronico` varchar(50) NOT NULL,
  `barrio` varchar(50) NOT NULL,
  `calle` text NOT NULL,
  `numero` bigint(20) NOT NULL,
  `pais` varchar(50) NOT NULL,
  `provincia` varchar(50) NOT NULL,
  `IDTurnoPaciente` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pacientes`
--

INSERT INTO `pacientes` (`IDPacientes`, `nombre`, `apellido`, `fechaNacimiento`, `genero`, `cuit`, `telefonoCelular`, `correoElectronico`, `barrio`, `calle`, `numero`, `pais`, `provincia`, `IDTurnoPaciente`) VALUES
(2, 'Santiago', 'Aranda', '2023-12-13', 'Masculino', 123, 123, 'santiago.aranda.@gmail.com', '2de Abril', 'Av italia', 200, 'Argentina', 'Formosa', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagos`
--

CREATE TABLE `pagos` (
  `IDPago` bigint(20) NOT NULL,
  `tipoDePago` enum('Efectivo','OrdenMedica') NOT NULL,
  `fechaPago` date NOT NULL,
  `coberturaMedica` enum('Si','No') NOT NULL,
  `ordenMedica` enum('Si','No') NOT NULL,
  `pagoPaciente` enum('Pago','Cobertura') NOT NULL,
  `ingresoPago` bigint(20) NOT NULL,
  `OrdenesMedicas` bigint(20) NOT NULL,
  `IDConsulta` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `turnero`
--

CREATE TABLE `turnero` (
  `IDTurnos` bigint(20) NOT NULL,
  `IDTurnoMedico` bigint(20) NOT NULL,
  `IDConsultorio` bigint(20) NOT NULL,
  `IDPaciente` bigint(20) NOT NULL,
  `estado` enum('Libre','Otorgado','En sala','En consultorio','Reasignado') NOT NULL,
  `horariosTurnos` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `consulta`
--
ALTER TABLE `consulta`
  ADD PRIMARY KEY (`IDConsulta`),
  ADD KEY `IDTurnero` (`IDTurnero`);

--
-- Indices de la tabla `consultorio`
--
ALTER TABLE `consultorio`
  ADD PRIMARY KEY (`IDConsultorio`);

--
-- Indices de la tabla `historialclinico`
--
ALTER TABLE `historialclinico`
  ADD PRIMARY KEY (`IDHistorialClinico`),
  ADD KEY `IDConsulta` (`IDConsulta`);

--
-- Indices de la tabla `horariosmedicos`
--
ALTER TABLE `horariosmedicos`
  ADD PRIMARY KEY (`IDTurnoMedico`),
  ADD KEY `IDMedico` (`IDMedico`);

--
-- Indices de la tabla `medicos`
--
ALTER TABLE `medicos`
  ADD PRIMARY KEY (`IDMedicos`),
  ADD KEY `IDEspecialidad` (`especialidad`);

--
-- Indices de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  ADD PRIMARY KEY (`IDPacientes`),
  ADD KEY `IDTurnoPaciente` (`IDTurnoPaciente`);

--
-- Indices de la tabla `pagos`
--
ALTER TABLE `pagos`
  ADD PRIMARY KEY (`IDPago`),
  ADD KEY `IDConsulta` (`IDConsulta`);

--
-- Indices de la tabla `turnero`
--
ALTER TABLE `turnero`
  ADD PRIMARY KEY (`IDTurnos`),
  ADD KEY `IDTurnoMedico` (`IDTurnoMedico`,`IDConsultorio`,`IDPaciente`),
  ADD KEY `IDConsultorio` (`IDConsultorio`),
  ADD KEY `IDPaciente` (`IDPaciente`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `consulta`
--
ALTER TABLE `consulta`
  MODIFY `IDConsulta` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `consultorio`
--
ALTER TABLE `consultorio`
  MODIFY `IDConsultorio` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `historialclinico`
--
ALTER TABLE `historialclinico`
  MODIFY `IDHistorialClinico` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `horariosmedicos`
--
ALTER TABLE `horariosmedicos`
  MODIFY `IDTurnoMedico` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `medicos`
--
ALTER TABLE `medicos`
  MODIFY `IDMedicos` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  MODIFY `IDPacientes` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `pagos`
--
ALTER TABLE `pagos`
  MODIFY `IDPago` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `turnero`
--
ALTER TABLE `turnero`
  MODIFY `IDTurnos` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `consulta`
--
ALTER TABLE `consulta`
  ADD CONSTRAINT `consulta_ibfk_1` FOREIGN KEY (`IDTurnero`) REFERENCES `turnero` (`IDTurnos`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `historialclinico`
--
ALTER TABLE `historialclinico`
  ADD CONSTRAINT `historialclinico_ibfk_1` FOREIGN KEY (`IDConsulta`) REFERENCES `consulta` (`IDConsulta`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `horariosmedicos`
--
ALTER TABLE `horariosmedicos`
  ADD CONSTRAINT `horariosmedicos_ibfk_1` FOREIGN KEY (`IDMedico`) REFERENCES `medicos` (`IDMedicos`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `pagos`
--
ALTER TABLE `pagos`
  ADD CONSTRAINT `pagos_ibfk_1` FOREIGN KEY (`IDConsulta`) REFERENCES `consulta` (`IDConsulta`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `turnero`
--
ALTER TABLE `turnero`
  ADD CONSTRAINT `turnero_ibfk_1` FOREIGN KEY (`IDConsultorio`) REFERENCES `consultorio` (`IDConsultorio`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `turnero_ibfk_2` FOREIGN KEY (`IDTurnoMedico`) REFERENCES `horariosmedicos` (`IDTurnoMedico`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `turnero_ibfk_3` FOREIGN KEY (`IDPaciente`) REFERENCES `pacientes` (`IDPacientes`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
