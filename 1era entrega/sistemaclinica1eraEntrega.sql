-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 01-06-2023 a las 21:10:33
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sistemaclinica1`
--

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
-- Estructura de tabla para la tabla `entidades`
--

CREATE TABLE `entidades` (
  `IDEntidad` bigint(20) NOT NULL,
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
  `provincia` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `especialidad`
--

CREATE TABLE `especialidad` (
  `IDEspecialidad` bigint(20) NOT NULL,
  `especialidad` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historialclinico`
--

CREATE TABLE `historialclinico` (
  `IDHistorialClinico` bigint(20) NOT NULL,
  `historialPaciente` varchar(50) NOT NULL,
  `diagnostico` varchar(50) NOT NULL,
  `ultimaActualizacion` date NOT NULL,
  `IDMedico` bigint(20) NOT NULL,
  `IDPaciente` bigint(20) NOT NULL,
  `IDTurnos` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `horariosmedicos`
--

CREATE TABLE `horariosmedicos` (
  `IDTurnoMedico` bigint(20) NOT NULL,
  `horarioMedico` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medicos`
--

CREATE TABLE `medicos` (
  `IDMedicos` bigint(20) NOT NULL,
  `IDEntidad` bigint(20) NOT NULL,
  `IDEspecialidad` bigint(20) NOT NULL,
  `IDTurnoMedico` bigint(20) NOT NULL,
  `IDConsultorio` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pacientes`
--

CREATE TABLE `pacientes` (
  `IDPacientes` bigint(20) NOT NULL,
  `IDEntidad` bigint(20) NOT NULL,
  `IDTurnoPaciente` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  `IDPaciente` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `turnero`
--

CREATE TABLE `turnero` (
  `IDTurnos` bigint(20) NOT NULL,
  `IDMedico` bigint(20) NOT NULL,
  `IDTurnoMedico` bigint(20) NOT NULL,
  `IDPagos` bigint(20) NOT NULL,
  `IDConsultorio` bigint(20) NOT NULL,
  `IDPaciente` bigint(20) NOT NULL,
  `estado` enum('Libre','Otorgado','En sala','En consultorio','Reasignado') NOT NULL,
  `horariosTurnos` datetime NOT NULL,
  `derivaciones` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `consultorio`
--
ALTER TABLE `consultorio`
  ADD PRIMARY KEY (`IDConsultorio`);

--
-- Indices de la tabla `entidades`
--
ALTER TABLE `entidades`
  ADD PRIMARY KEY (`IDEntidad`);

--
-- Indices de la tabla `especialidad`
--
ALTER TABLE `especialidad`
  ADD PRIMARY KEY (`IDEspecialidad`);

--
-- Indices de la tabla `historialclinico`
--
ALTER TABLE `historialclinico`
  ADD PRIMARY KEY (`IDHistorialClinico`),
  ADD KEY `IDMedico` (`IDMedico`,`IDPaciente`,`IDTurnos`),
  ADD KEY `IDPaciente` (`IDPaciente`),
  ADD KEY `IDTurnos` (`IDTurnos`);

--
-- Indices de la tabla `horariosmedicos`
--
ALTER TABLE `horariosmedicos`
  ADD PRIMARY KEY (`IDTurnoMedico`);

--
-- Indices de la tabla `medicos`
--
ALTER TABLE `medicos`
  ADD PRIMARY KEY (`IDMedicos`),
  ADD KEY `IDEntidad` (`IDEntidad`,`IDEspecialidad`,`IDTurnoMedico`,`IDConsultorio`),
  ADD KEY `IDEspecialidad` (`IDEspecialidad`),
  ADD KEY `IDConsultorio` (`IDConsultorio`),
  ADD KEY `IDTurnoMedico` (`IDTurnoMedico`);

--
-- Indices de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  ADD PRIMARY KEY (`IDPacientes`),
  ADD KEY `IDEntidad` (`IDEntidad`),
  ADD KEY `IDTurnoPaciente` (`IDTurnoPaciente`);

--
-- Indices de la tabla `pagos`
--
ALTER TABLE `pagos`
  ADD PRIMARY KEY (`IDPago`),
  ADD KEY `IDPaciente` (`IDPaciente`);

--
-- Indices de la tabla `turnero`
--
ALTER TABLE `turnero`
  ADD PRIMARY KEY (`IDTurnos`),
  ADD KEY `IDMedico` (`IDMedico`,`IDTurnoMedico`,`IDPagos`,`IDConsultorio`,`IDPaciente`),
  ADD KEY `IDTurnoMedico` (`IDTurnoMedico`),
  ADD KEY `IDConsultorio` (`IDConsultorio`),
  ADD KEY `IDPaciente` (`IDPaciente`),
  ADD KEY `IDPagos` (`IDPagos`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `historialclinico`
--
ALTER TABLE `historialclinico`
  ADD CONSTRAINT `historialclinico_ibfk_1` FOREIGN KEY (`IDMedico`) REFERENCES `medicos` (`IDMedicos`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `historialclinico_ibfk_2` FOREIGN KEY (`IDPaciente`) REFERENCES `pacientes` (`IDPacientes`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `historialclinico_ibfk_3` FOREIGN KEY (`IDTurnos`) REFERENCES `turnero` (`IDTurnos`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `medicos`
--
ALTER TABLE `medicos`
  ADD CONSTRAINT `medicos_ibfk_1` FOREIGN KEY (`IDEntidad`) REFERENCES `entidades` (`IDEntidad`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `medicos_ibfk_2` FOREIGN KEY (`IDEspecialidad`) REFERENCES `especialidad` (`IDEspecialidad`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `medicos_ibfk_3` FOREIGN KEY (`IDConsultorio`) REFERENCES `consultorio` (`IDConsultorio`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `medicos_ibfk_4` FOREIGN KEY (`IDTurnoMedico`) REFERENCES `horariosmedicos` (`IDTurnoMedico`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `pacientes`
--
ALTER TABLE `pacientes`
  ADD CONSTRAINT `pacientes_ibfk_1` FOREIGN KEY (`IDEntidad`) REFERENCES `entidades` (`IDEntidad`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `pacientes_ibfk_2` FOREIGN KEY (`IDTurnoPaciente`) REFERENCES `turnero` (`IDTurnos`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `pagos`
--
ALTER TABLE `pagos`
  ADD CONSTRAINT `pagos_ibfk_1` FOREIGN KEY (`IDPaciente`) REFERENCES `pacientes` (`IDPacientes`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `turnero`
--
ALTER TABLE `turnero`
  ADD CONSTRAINT `turnero_ibfk_1` FOREIGN KEY (`IDTurnoMedico`) REFERENCES `horariosmedicos` (`IDTurnoMedico`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `turnero_ibfk_2` FOREIGN KEY (`IDConsultorio`) REFERENCES `consultorio` (`IDConsultorio`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `turnero_ibfk_3` FOREIGN KEY (`IDPaciente`) REFERENCES `pacientes` (`IDPacientes`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `turnero_ibfk_4` FOREIGN KEY (`IDPagos`) REFERENCES `pagos` (`IDPago`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `turnero_ibfk_5` FOREIGN KEY (`IDMedico`) REFERENCES `medicos` (`IDMedicos`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
