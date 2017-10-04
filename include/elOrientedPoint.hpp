#ifndef __ELORIENTEDPOINT_HPP
#define __ELORIENTEDPOINT_HPP
/******************************************************************************
 *
 * Copyright (c) 2004-2005, Samuli Laine
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without modification,
 * are permitted provided that the following conditions are met:
 *
 *  - Redistributions of source code must retain the above copyright notice,
 *    this list of conditions and the following disclaimer.
 *  - Redistributions in binary form must reproduce the above copyright notice,
 *    this list of conditions and the following disclaimer in the documentation
 *    and/or other materials provided with the distribution.
 *  - Neither the name of the copyright holder nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
 * IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
 * INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 * NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
 * OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
 * WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */

#if !defined (__ELVECTOR_HPP)
#	include "elVector.hpp"
#endif

namespace EL
{

//------------------------------------------------------------------------

class OrientedPoint
{
public:
									OrientedPoint	(void);
									OrientedPoint	(const OrientedPoint& s);
									~OrientedPoint	(void);

	const OrientedPoint&			operator=		(const OrientedPoint& s);

	EL_FORCE_INLINE const Vector3&	getPosition		(void) const					{ return m_position; }
	EL_FORCE_INLINE const Matrix3&	getOrientation	(void) const					{ return m_orientation; }
	void							setPosition		(const Vector3& position)		{ m_position = position; }
	void							setOrientation	(const Matrix3& orientation)	{ m_orientation = orientation; }
	void							translate		(const Vector3& translation)	{ m_position += translation; }
	void							rotate			(const Matrix3& rotation)		{ m_orientation *= rotation; }

	const std::string&				getName			(void) const					{ return m_name; }
	void							setName			(std::string name)				{ m_name = name; }

	Vector3							getDirection	(void) const					{ return m_orientation.getColumn(2); }
	Vector3							getUp			(void) const					{ return m_orientation.getColumn(1); }
	Vector3							getRight		(void) const					{ return m_orientation.getColumn(0); }

	void							render			(const Vector3& color) const;

private:
	Vector3							m_position;
	Matrix3							m_orientation;
	std::string						m_name;
};

//------------------------------------------------------------------------
} // namespace EL

#endif // __ELORIENTEDPOINT_HPP
